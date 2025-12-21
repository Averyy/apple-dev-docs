# CMFormatDescriptionEqualIgnoringExtensionKeys(_:otherFormatDescription:extensionKeysToIgnore:sampleDescriptionExtensionAtomKeysToIgnore:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether two format descriptions are equal, ignoring differences in the extension keys you specify.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMFormatDescriptionEqualIgnoringExtensionKeys(_ formatDescription: CMFormatDescription?, otherFormatDescription: CMFormatDescription?, extensionKeysToIgnore formatDescriptionExtensionKeysToIgnore: CFTypeRef?, sampleDescriptionExtensionAtomKeysToIgnore: CFTypeRef?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the two descriptions are equal; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When you specify any keys, the function ignores `kCMFormatDescriptionExtension_VerbatimSampleDescription` and `kCMFormatDescriptionExtension_VerbatimISOSampleEntry` for the purpose of comparison.

> **Note**:  This function is `NULL` safe.

For extension atom keys, see [`kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms`](kcmformatdescriptionextension_sampledescriptionextensionatoms.md).

## Parameters

- `formatDescription`: The first description to compare.
- `otherFormatDescription`: The second description to compare.
- `formatDescriptionExtensionKeysToIgnore`: A single format description extension key ( ) or an array ( ) of keys.
- `sampleDescriptionExtensionAtomKeysToIgnore`: A single sample description extension atom key (four-character  ) or an array ( ) of such keys.

## See Also

- [func CMFormatDescriptionEqual(CMFormatDescription?, otherFormatDescription: CMFormatDescription?) -> Bool](cmformatdescriptionequal(_:otherformatdescription:).md)
  Returns a Boolean value that indicates whether two format descriptions are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptionequalignoringextensionkeys(_:otherformatdescription:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:))*