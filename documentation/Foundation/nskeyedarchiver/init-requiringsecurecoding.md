# init(requiringSecureCoding:)

**Framework**: Foundation  
**Kind**: init

Creates an archiver to encode data, and optionally disables secure coding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(requiringSecureCoding requiresSecureCoding: Bool)
```

#### Discussion

To prevent the possibility of encoding an object that [`NSKeyedUnarchiver`](nskeyedunarchiver.md) can’t decode, set `requiresSecureCoding` to [`true`](https://developer.apple.com/documentation/swift/true) whenever possible. This ensures that all encoded objects conform to [`NSSecureCoding`](nssecurecoding.md).

> **Note**:  Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## Parameters

- `requiresSecureCoding`: A Boolean value indicating whether all encoded objects must conform to  .

## See Also

- [var requiresSecureCoding: Bool](nskeyedarchiver/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [init()](nskeyedarchiver/init.md)
  Initializes an archiver to encode data.
- [init(forWritingWith: NSMutableData)](nskeyedarchiver/init(forwritingwith:).md)
  Initializes an archiver to encode data into a given a mutable-data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/init(requiringsecurecoding:))*