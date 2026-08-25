# Removed commands and profiles

**Framework**: Device Management

Commands and configuration profiles that have been removed and are no longer supported.

## Topics

### Commands
- [Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.
- [OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.
- [Schedule OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.
- [Schedule OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.
### Profiles
- [object SoftwareUpdate](softwareupdate.md)
  The payload that configures the software update policy. Removed: use the declarative management `com.apple.configuration.softwareupdate.settings` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/removed-commands-and-profiles)*