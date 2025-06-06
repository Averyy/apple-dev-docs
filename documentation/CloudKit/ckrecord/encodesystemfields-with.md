# encodeSystemFields(with:)

**Framework**: CloudKit  
**Kind**: method

Encodes the record’s system fields using the specified archiver.

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
func encodeSystemFields(with coder: NSCoder)
```

#### Discussion

Use this method to encode the record’s metadata that CloudKit provides. Every record has keys that the system defines that correspond to record metadata, such as the record ID, record type, creation date, and so on. This method encodes those keys in the specified archiver. This method doesn’t include any keys you add to the record. It also doesn’t encode the keys that the [`changedKeys`](ckrecord/changedkeys.md) method returns.

You might use this method when you want to store only the system metadata because you store the actual record data elsewhere.

## Parameters

- `coder`: An archiver object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/encodesystemfields(with:))*