---
url: "https://docs.swift.org/latest/documentation/embeddedswift/rpi5blinkguide"
framework: "Swift-Org/EmbeddedSwift"
---

# Blinking an LED on the Raspberry Pi 5

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article  
**Download**: [rpi-5-blink](https://github.com/swiftlang/swift-embedded-examples/tree/main/rpi-5-blink)

Run a baremetal Swift MMIO program that blinks the Raspberry Pi 5’s status LED, with no SDK or operating system.

## Overview

This example demonstrates how to build a baremetal Embedded Swift kernel image for the Raspberry Pi 5 using Swift MMIO for type-safe register access, without depending on an SDK. The Swift code toggles the board’s green (ACT) status LED, which is wired through the RP1 southbridge chip’s GPIO controller. See [Blinking an LED on the Raspberry Pi 4B](./rpi4bblinkguide.md) for the closely related Raspberry Pi 4B example — the two differ mainly in their GPIO register offsets and base address, since the Pi 5 drives its LED through the RP1 chip instead of the SoC’s own GPIO controller.

The GPIO registers are described as Swift MMIO register types, and an `Application` entry point configures the pin as an output and toggles it in an infinite loop:

```swift
@RegisterBlock
struct GPIO {
  @RegisterBlock(offset: 0x00008)
  var gioiodir: Register<GIOIODIR>
  @RegisterBlock(offset: 0x00004)
  var giodata: Register<GIODATA>
}

let gpio = GPIO(unsafeAddress: 0x10_7d51_7c00)

@main
struct Application {
  static func main() {
    setLedOutput()
    while true {
      ledOn()
      delay()
      ledOff()
      delay()
    }
  }
}
```

> **Note**: This is a baremetal example — there’s no SDK or operating system involved. See [Using Embedded Swift in baremetal mode](./baremetal.md) for general guidance on baremetal Embedded Swift development.

## Install Swift

Follow the instructions in [Installing Embedded Swift](./installembeddedswift.md) to install the latest Swift development snapshot with Embedded Swift support. Confirm the installation by running `swift --version` — it reports a “6.2-dev” or newer development snapshot.

## Prepare an SD card

Prepare an SD card with a Raspberry Pi OS install on it, so the required boot partition and configuration files already exist. Back up `kernel8.img` and `kernel_2712.img` from the SD card if you need the Linux install later, since this example replaces one of these kernel images.

## Build the project

Navigate to the example directory and build it:

```shell
$ cd rpi-5-blink
$ make
```

This produces `.build/aarch64-none-none-elf/release/Application.bin`, the raw kernel image extracted from the built ELF executable.

## Run on a device

Copy the kernel image to the SD card’s boot partition, and remove the existing `kernel_2712.img` so the Raspberry Pi 5’s newer boot process picks up the Embedded Swift kernel instead:

```shell
$ cp .build/aarch64-none-none-elf/release/Application.bin /Volumes/bootfs/kernel8.img
$ rm /Volumes/bootfs/kernel_2712.img
```

Alternatively, rename `Application.bin` to `kernel_2712.img` directly, or set a custom kernel filename with the `kernel=` setting in `config.txt`.

Place the SD card in the Raspberry Pi 5 and connect it to power. After the boot sequence, the green (ACT) LED blinks in a regular pattern.

## See Also

### Raspberry Pi examples
- [Blinking an LED on the Raspberry Pi 4B](./rpi4bblinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 4B’s status LED, with no SDK or operating system.
- [Blinking an LED in Morse code on the Raspberry Pi Pico W with the Pico SDK](./rpipicowblinkguide.md)
  Run a Swift program on a Raspberry Pi Pico W or Pico 2 W that signals “SOS” in Morse code using the Pico SDK’s Wi-Fi chip driver.
- [Blinking an LED in Morse code on the Raspberry Pi Pico](./rpipicoblinkguide.md)
  Run a baremetal Swift program on a Raspberry Pi Pico that spells “Hello Swift!” in Morse code on the onboard LED, with no SDK or operating system.
- [Driving a NeoPixel LED on the Raspberry Pi Pico 2](./rpipico2neopixelguide.md)
  Run a baremetal Swift program that drives a WS2812 NeoPixel RGB LED from an RP2350’s PIO block, with no SDK or operating system.
- [Building Harmony, a Bluetooth speaker and ferrofluid visualizer](./harmonyguide.md)
  Build and flash Harmony, a Raspberry Pi Pico W firmware in Swift that streams Bluetooth audio and drives a ferrofluid visualizer.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/rpi5blinkguide)*