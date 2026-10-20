# ManagedSettingsStore.Name

**Framework**: Managed Settings  
**Kind**: struct  
**Role**: Structure

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
- [init(String)](./name/init%28_%29.md)
  Creates a new instance with the specified string.
- [init(rawValue: String)](./name/init%28rawvalue%29.md)
  Creates a new instance with the specified string.
### Instance Properties
- [let rawValue: String](./name/rawvalue.md)
  The name of the store as a `String`.
### Type Properties
- [static let `default`: ManagedSettingsStore.Name](./name/default.md)
  The default store name.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore/name)*