# writePropertyList(_:to:format:options:error:)

**Framework**: Foundation  
**Kind**: method

Writes a property list to the specified stream.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func writePropertyList(_ plist: Any, to stream: OutputStream, format: PropertyListSerialization.PropertyListFormat, options opt: PropertyListSerialization.WriteOptions, error: NSErrorPointer) -> Int
```

#### Return Value

The number of bytes written to the stream. A return value of `0` indicates that an error occurred.

## Parameters

- `plist`: The property list that you want to write out.
- `stream`: An   instance that is open and ready to receive the property list data.
- `format`: One of the property list formats defined in  .
- `opt`: Currently unused. Set to  .
- `error`: A pointer that the function may set to an   object when an error occurs to provide additional information about the error.

## See Also

- [class func data(fromPropertyList: Any, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions) throws -> Data](propertylistserialization/data(frompropertylist:format:options:).md)
  Returns an `NSData` object containing a given property list in a specified format.
- [PropertyListSerialization.WriteOptions](propertylistserialization/writeoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/writepropertylist(_:to:format:options:error:))*