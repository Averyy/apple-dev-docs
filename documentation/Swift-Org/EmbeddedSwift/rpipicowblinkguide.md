---
url: "https://docs.swift.org/latest/documentation/embeddedswift/rpipicowblinkguide"
framework: "Swift-Org/EmbeddedSwift"
---

# Blinking an LED in Morse code on the Raspberry Pi Pico W with the Pico SDK

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article  
**Download**: [rpi-picow-blink-sdk](https://github.com/swiftlang/swift-embedded-examples/tree/main/rpi-picow-blink-sdk)

Run a Swift program on a Raspberry Pi Pico W or Pico 2 W that signals “SOS” in Morse code using the Pico SDK’s Wi-Fi chip driver.

## Overview

This example demonstrates how to integrate with the Pico SDK’s CMake build system on a Wi-Fi-enabled Pico board. Unlike the plain Raspberry Pi Pico, the Pico W and Pico 2 W don’t wire their LED directly to a GPIO pin — it’s attached to the onboard CYW43439 wireless chip instead, so the LED is controlled through the `cyw43_arch` driver rather than the regular GPIO API. See [Blinking an LED on the Raspberry Pi Pico with the Pico SDK](./rpipicoguide.md) for the CMake and Pico SDK integration this example builds on for the non-Wi-Fi Pico.

The Swift code initializes the Wi-Fi chip driver, then toggles its LED in a loop that spells “SOS” using dots and dashes:

```swift
@main
struct Main {
  static func main() {
    let led = UInt32(CYW43_WL_GPIO_LED_PIN)
    if cyw43_arch_init() != 0 {
      print("Wi-Fi init failed")
      return
    }
    let dot = {
      cyw43_arch_gpio_put(led, true)
      sleep_ms(250)
      cyw43_arch_gpio_put(led, false)
      sleep_ms(250)
    }
    let dash = {
      cyw43_arch_gpio_put(led, true)
      sleep_ms(500)
      cyw43_arch_gpio_put(led, false)
      sleep_ms(250)
    }
    while true {
      dot(); dot(); dot()
      dash(); dash(); dash()
      dot(); dot(); dot()
    }
  }
}
```

## Install dependencies

- A Raspberry Pi Pico W or Pico 2 W board. If you have a plain Pico (non-W) instead, see [Blinking an LED on the Raspberry Pi Pico with the Pico SDK](./rpipicoguide.md) or the [rpi-pico-blink-sdk](https://github.com/swiftlang/swift-embedded-examples/tree/main/rpi-pico-blink-sdk) example instead.
- Follow the setup steps in the [Pico “Getting Started” guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf). In particular, you’ll need:

  - A checkout of the [pico-sdk](https://github.com/raspberrypi/pico-sdk.git), with git submodules checked out.
  - A checkout of the [pico-examples](https://github.com/raspberrypi/pico-examples.git).
  - CMake.
  - The [Arm Embedded Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).

Before adding Swift, confirm that your setup can build the standard C/C++ sample projects. A good test is building and running the “blink” example from pico-examples.

## Install Swift

Follow the instructions in [Installing Embedded Swift](./installembeddedswift.md) to install the latest Swift development snapshot with Embedded Swift support. Confirm the installation by running `swift --version` — it reports a “6.2-dev” or newer development snapshot.

## Build the project

Navigate to the example directory, set the required environment variables, and configure the build:

```shell
$ cd rpi-picow-blink-sdk
$ export PICO_BOARD=pico_w  # or pico2_w
$ export PICO_SDK_PATH='<path-to-your-pico-sdk>'
$ export PICO_TOOLCHAIN_PATH='<path-to-the-arm-toolchain>'
$ cmake -B build -G Ninja . -DCMAKE_EXPORT_COMPILE_COMMANDS=On
```

Build the project:

```shell
$ cmake --build build
```

## Run on a device

Connect the Pico W board to your Mac using USB, and make sure it’s in USB Mass Storage firmware upload mode (hold the BOOTSEL button while plugging in the board, or make sure the flash memory doesn’t already contain valid firmware).

Copy the UF2 firmware to the mounted volume:

```shell
$ cp build/swift-blinky.uf2 /Volumes/RP2040  # or /Volumes/RP2350 for Pico 2 W
```

The LED blinks the “SOS” pattern in Morse code repeatedly.

## See Also

### Raspberry Pi examples
- [Blinking an LED on the Raspberry Pi 4B](./rpi4bblinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 4B’s status LED, with no SDK or operating system.
- [Blinking an LED on the Raspberry Pi 5](./rpi5blinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 5’s status LED, with no SDK or operating system.
- [Blinking an LED in Morse code on the Raspberry Pi Pico](./rpipicoblinkguide.md)
  Run a baremetal Swift program on a Raspberry Pi Pico that spells “Hello Swift!” in Morse code on the onboard LED, with no SDK or operating system.
- [Driving a NeoPixel LED on the Raspberry Pi Pico 2](./rpipico2neopixelguide.md)
  Run a baremetal Swift program that drives a WS2812 NeoPixel RGB LED from an RP2350’s PIO block, with no SDK or operating system.
- [Building Harmony, a Bluetooth speaker and ferrofluid visualizer](./harmonyguide.md)
  Build and flash Harmony, a Raspberry Pi Pico W firmware in Swift that streams Bluetooth audio and drives a ferrofluid visualizer.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/rpipicowblinkguide)*