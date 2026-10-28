# CMFormatDescriptionEqual(_:otherFormatDescription:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CMFormatDescriptionEqual(CMFormatDescriptionRef formatDescription, CMFormatDescriptionRef otherFormatDescription);
```

## Return Value

[`true`](../Swift/true.md) if the two descriptions are equal; otherwise, [`false`](../Swift/false.md).

## Discussion

This calls `CFEqual` on the provided `CMFormatDescription` objects. In contrast to the Core Foundation call it is `NULL` safe.

## Parameters

- `formatDescription`: The first description to compare.
- `otherFormatDescription`: The second description to compare.

## See Also

### Comparing Format Descriptions
- [func CMFormatDescriptionEqualIgnoringExtensionKeys(CMFormatDescription?, otherFormatDescription: CMFormatDescription?, extensionKeysToIgnore: CFTypeRef?, sampleDescriptionExtensionAtomKeysToIgnore: CFTypeRef?) -> Bool](./cmformatdescriptionequalignoringextensionkeys%28_,otherformatdescription,extensionkeystoignore,sampledescriptionextensionatomkeystoignore%29.md)
  Returns a Boolean value that indicates whether two format descriptions are equal, ignoring differences in the extension keys you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptionequal(_:otherformatdescription:))*