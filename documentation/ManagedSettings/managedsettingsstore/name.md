# ManagedSettingsStore.Name

**Framework**: ManagedSettings  
**Kind**: struct

The unique name of a store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Name
```

#### Overview

Use `ManagedSettingsStore.Name` to create distinct stores with their own settings. Initializing multiple stores with the same name will share settings.

## Topics

### Initializers
- [init(String)](managedsettingsstore/name/init(_:).md)
  Creates a new instance with the specified string.
- [init(rawValue: String)](managedsettingsstore/name/init(rawvalue:).md)
  Creates a new instance with the specified string.
### Instance Properties
- [let rawValue: String](managedsettingsstore/name/rawvalue.md)
  The name of the store as a `String`.
### Type Properties
- [static let `default`: ManagedSettingsStore.Name](managedsettingsstore/name/default.md)
  The default store name.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore/name)*