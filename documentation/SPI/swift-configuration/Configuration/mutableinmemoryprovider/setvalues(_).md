---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/setvalues(_:)"
framework: "swift-configuration/Configuration"
---

# setValues(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Updates the stored values for multiple configuration keys at once.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func setValues(_ values: [AbsoluteConfigKey : ConfigValue?])
```

## Mentions

- [Using in-memory providers](../using-in-memory-providers.md)

## Discussion

This method atomically applies all the updates, so a snapshot never contains some of the updates without the others. Watchers of a changed key receive its new value once. If any value changed, snapshot watchers receive one snapshot that contains all the updates. If a new value is the same as the existing value, no notification is sent for that key.

Keys not included in `values` keep their current values.

```swift
let provider = MutableInMemoryProvider(initialValues: [
    "database.timeout": 15,
    "database.replicationStrategy": "sameRegion"
])

provider.setValues([
    "database.host": "db-a.example.com",
    "database.port": 5433,
    "database.timeout": nil, // Removes the value
])

// Values are now:
// "database.host": "db-a.example.com",
// "database.port": 5433,
// "database.replicationStrategy": "sameRegion"
```

If you build `values` in code, assigning `nil` with the subscript removes the key from the dictionary, so the provider keeps that key’s current value. To remove a value, assign `.some(nil)` instead:

```swift
var updates: [AbsoluteConfigKey: ConfigValue?] = [:]
updates["database.port"] = 5433

// Don't: this removes the key from `updates`, so the provider keeps the current value.
updates["database.timeout"] = nil

// Do: this keeps the key with a `nil` value, so the provider removes the value.
updates["database.timeout"] = .some(nil)

provider.setValues(updates)
```

Alternatively, make the changes in [`withValues(_:)`](./withvalues%28_%29.md), where assigning `nil` removes the value.

## Parameters

- `values`: A dictionary that maps configuration keys to their new values, or to `nil` to remove a value entirely.

## See Also

### Updating values in a mutable in-memory provider
- [func setValue(ConfigValue?, forKey: AbsoluteConfigKey)](./setvalue%28_,forkey%29.md)
  Updates the stored value for the specified configuration key.
- [func withValues<Return, Failure>((inout [AbsoluteConfigKey : ConfigValue]) throws(Failure) -> Return) throws(Failure) -> Return](./withvalues%28_%29.md)
  Reads and updates the stored values in a single atomic operation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/setvalues(_:))*