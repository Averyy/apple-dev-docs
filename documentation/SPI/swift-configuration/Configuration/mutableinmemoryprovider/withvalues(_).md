---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/withvalues(_:)"
framework: "swift-configuration/Configuration"
---

# withValues(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Reads and updates the stored values in a single atomic operation.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func withValues<Return, Failure>(_ body: (inout [AbsoluteConfigKey : ConfigValue]) throws(Failure) -> Return) throws(Failure) -> Return where Failure : Error, Return : ~Copyable
```

## Mentions

- [Using in-memory providers](../using-in-memory-providers.md)

## Return Value

The value that `body` returns.

## Discussion

The body runs while the provider holds its lock, so no other reads or updates happen until it finishes. It edits the stored values in place: if the body throws, the changes it made before the error are kept. When the body returns or throws, watchers of changed keys receive their new values. If any value changed, snapshot watchers receive one snapshot that contains all the changes.

Don’t call the provider, or a [`ConfigReader`](../configreader.md) that reads from it, from inside the body. The lock isn’t recursive, so the call crashes or deadlocks.

```swift
provider.withValues { values in
    if values["database.host"] == "db-a.example.com" {
        values["database.host"] = "db-b.example.com"
        values["database.port"] = 6432
    }
}
```

> **Throws**: Rethrows any error that `body` throws.

## Parameters

- `body`: A closure that reads and modifies the stored values.

## See Also

### Updating values in a mutable in-memory provider
- [func setValue(ConfigValue?, forKey: AbsoluteConfigKey)](./setvalue%28_,forkey%29.md)
  Updates the stored value for the specified configuration key.
- [func setValues([AbsoluteConfigKey : ConfigValue?])](./setvalues%28_%29.md)
  Updates the stored values for multiple configuration keys at once.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider/withvalues(_:))*