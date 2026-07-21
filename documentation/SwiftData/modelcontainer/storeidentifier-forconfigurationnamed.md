# storeIdentifier(forConfigurationNamed:)

**Framework**: SwiftData  
**Kind**: method

Returns the on-disk store identifier for the given configuration name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Swift 5.9+

## Declaration

```swift
func storeIdentifier(forConfigurationNamed name: String) -> String?
```

#### Return Value

The store identifier string, or `nil` if no store is associated with `name` or if `invalidate()` has been called on this container.

#### Discussion

Store identifiers are stable strings derived from the backing file path or the store’s own initialization — they are *not* the configuration name. Use this function when you have the name you passed to `ModelConfiguration` and need the corresponding identifier to filter a `HistoryDescriptor`, interpret `PersistentIdentifier.storeIdentifier`, or route to a specific store.

If no `ModelConfiguration` was given an explicit name at initialization time, the default name is `"default"`.

## Parameters

- `name`: The `name` value from the `ModelConfiguration` used to create the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer/storeidentifier(forconfigurationnamed:))*