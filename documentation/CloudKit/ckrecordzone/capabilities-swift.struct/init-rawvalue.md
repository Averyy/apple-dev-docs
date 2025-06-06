# init(rawValue:)

**Framework**: CloudKit  
**Kind**: init

Creates a set of capabilities for a record zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(rawValue: UInt)
```

#### Discussion

Capabilities on record zones that you create locally aren’t valid until you save the record zone. Capabilities on record zones that you fetch from the server are always valid.

## Parameters

- `rawValue`: An integer that represents the combined set of capabilities to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.struct/init(rawvalue:))*