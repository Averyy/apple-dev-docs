# init(named:)

**Framework**: Managed Settings  
**Kind**: init

Creates a new instance of a store with a custom name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+

## Declaration

```swift
convenience init(named name: ManagedSettingsStore.Name)
```

#### Discussion

Each store contains the settings that the client app applies. If the client app doesn’t explicitly apply a setting, the default value is `nil`. Using `.default` is akin to calling  `ManagedSettingsStore()`.

## Parameters

- `name`: A unique name for the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore/init(named:))*