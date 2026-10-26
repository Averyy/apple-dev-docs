---
url: "https://docs.swift.org/latest/documentation/embeddedswift/rpipicoblinkguide"
framework: "Swift-Org/EmbeddedSwift"
---

# Blinking an LED in Morse code on the Raspberry Pi Pico

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article  
**Download**: [rpi-pico-blink](https://github.com/swiftlang/swift-embedded-examples/tree/main/rpi-pico-blink)

Run a baremetal Swift program on a Raspberry Pi Pico that spells “Hello Swift!” in Morse code on the onboard LED, with no SDK or operating system.

#### Overview

This example demonstrates how to build a baremetal Embedded Swift kernel image for the Raspberry Pi Pico’s RP2040 chip from scratch, without depending on the Pico SDK. The package provides its own `RP2040` hardware abstraction layer that wraps the chip’s memory-mapped registers (GPIO, clocks, resets, the SIO block, and more), a `crt0.S` startup file, and a `Package.swift` built with a custom Mach-O toolset that gets converted to the UF2 firmware format. See [Blinking an LED on the Raspberry Pi Pico with the Pico SDK](./rpipicoguide.md) for the CMake-based Pico SDK approach to this same board.

The `Application` entry point configures the LED pin as an output, then loops forever, blinking out the message using dots and dashes:

```swift
import RP2040

@main
struct Application {
  static var board: RP2040! = nil

  static func main() {
    board = RP2040()
    board.setMode(.output, pin: .d22)

    let str: StaticString = "Hello Swift!"
    while true {
      str.withUTF8Buffer { buffer in
        for ch in buffer {
          emit(ch)
        }
        delay(7)
      }
    }
  }
}
```

> **Note**: This is a baremetal example — there’s no SDK or operating system involved. See [Using Embedded Swift in baremetal mode](./baremetal.md) for general guidance on baremetal Embedded Swift development.

#### Install Swift

Follow the instructions in [Installing Embedded Swift](./installembeddedswift.md) to install the latest Swift development snapshot with Embedded Swift support. Confirm the installation by running `swift --version` — it reports a “6.2-dev” or newer development snapshot.

#### Build the project

Navigate to the example directory and build it:

```shell
$ cd rpi-pico-blink
$ make
```

The Makefile drives `swift build` with a custom `armv6m-apple-none-macho` triple and toolset, then converts the resulting Mach-O binary to the UF2 firmware format using `Tools/macho2uf2.py`.

#### Run on a device

Connect the Pico board to your Mac using USB, and make sure it’s in USB Mass Storage firmware upload mode (hold the BOOTSEL button while plugging in the board, or make sure the flash memory doesn’t already contain valid firmware).

Copy the UF2 firmware to the mounted volume:

```shell
$ cp .build/armv6m-apple-none-macho/release/Application.uf2 /Volumes/RP2040
```

The onboard LED blinks the message in Morse code repeatedly.

## See Also

### Raspberry Pi examples
- [Blinking an LED on the Raspberry Pi 4B](./rpi4bblinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 4B’s status LED, with no SDK or operating system.
- [Blinking an LED on the Raspberry Pi 5](./rpi5blinkguide.md)
  Run a baremetal Swift MMIO program that blinks the Raspberry Pi 5’s status LED, with no SDK or operating system.
- [Blinking an LED in Morse code on the Raspberry Pi Pico W with the Pico SDK](./rpipicowblinkguide.md)
  Run a Swift program on a Raspberry Pi Pico W or Pico 2 W that signals “SOS” in Morse code using the Pico SDK’s Wi-Fi chip driver.
- [Driving a NeoPixel LED on the Raspberry Pi Pico 2](./rpipico2neopixelguide.md)
  Run a baremetal Swift program that drives a WS2812 NeoPixel RGB LED from an RP2350’s PIO block, with no SDK or operating system.
- [Building Harmony, a Bluetooth speaker and ferrofluid visualizer](./harmonyguide.md)
  Build and flash Harmony, a Raspberry Pi Pico W firmware in Swift that streams Bluetooth audio and drives a ferrofluid visualizer.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/rpipicoblinkguide)*