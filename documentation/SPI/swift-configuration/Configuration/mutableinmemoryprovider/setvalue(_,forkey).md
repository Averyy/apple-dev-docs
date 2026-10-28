---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/setvalue(_:forkey:)"
framework: "swift-configuration/Configuration"
---

# setValue(_:forKey:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Updates the stored value for the specified configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func setValue(_ value: ConfigValue?, forKey key: AbsoluteConfigKey)
```

## Discussion

This method atomically updates the value and notifies all active watchers of the change. If the new value is the same as the existing value, no notification is sent.

```swift
let provider = MutableInMemoryProvider(initialValues: [:])
let key = AbsoluteConfigKey(["api", "enabled"], context: [:])

// Set a new value
provider.setValue(true, forKey: key)

// Remove a value
provider.setValue(nil, forKey: key)
```

## Parameters

- `value`: The new configuration value, or `nil` to remove the value entirely.
- `key`: The absolute configuration key to update.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/setvalue(_:forkey:))*