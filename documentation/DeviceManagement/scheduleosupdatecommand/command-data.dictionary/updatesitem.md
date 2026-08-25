# ScheduleOSUpdateCommand.Command.UpdatesItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the available operating-system updates item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object ScheduleOSUpdateCommand.Command.UpdatesItem
```

## Properties

- `InstallAction` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `MaxUserDeferrals` (integer): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Priority` (string): ~~ Prior versions of macOS used a priority of `Low`.~~ 

Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductKey` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `ProductVersion` (string): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatecommand/command-data.dictionary/updatesitem)*