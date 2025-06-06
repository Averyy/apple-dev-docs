# CMFormatDescriptionEqual(_:otherFormatDescription:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether two format descriptions are equal.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMFormatDescriptionEqual(_ formatDescription: CMFormatDescription?, otherFormatDescription: CMFormatDescription?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the two descriptions are equal; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This calls `CFEqual` on the provided `CMFormatDescription` objects. In contrast to the Core Foundation call it is `NULL` safe.

## Parameters

- `formatDescription`: The first description to compare.
- `otherFormatDescription`: The second description to compare.

## See Also

- [func CMFormatDescriptionEqualIgnoringExtensionKeys(CMFormatDescription?, otherFormatDescription: CMFormatDescription?, extensionKeysToIgnore: CFTypeRef?, sampleDescriptionExtensionAtomKeysToIgnore: CFTypeRef?) -> Bool](cmformatdescriptionequalignoringextensionkeys(_:otherformatdescription:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:).md)
  Returns a Boolean value that indicates whether two format descriptions are equal, ignoring differences in the extension keys you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptionequal(_:otherformatdescription:))*