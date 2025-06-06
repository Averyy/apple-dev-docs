# writeJSONObject(_:to:options:error:)

**Framework**: Foundation  
**Kind**: method

Writes a given JSON object to a stream.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func writeJSONObject(_ obj: Any, to stream: OutputStream, options opt: JSONSerialization.WritingOptions = [], error: NSErrorPointer) -> Int
```

#### Return Value

The number of bytes written to the stream, or `0` if an error occurs.

## Parameters

- `obj`: The object to write to  .
- `stream`: The stream should be open and configured.
- `opt`: See   for possible values.
- `error`: If an error occurs, upon return contains an   object with code   that describes the problem.

## See Also

- [class func data(withJSONObject: Any, options: JSONSerialization.WritingOptions) throws -> Data](jsonserialization/data(withjsonobject:options:).md)
  Returns JSON data from a Foundation object.
- [JSONSerialization.WritingOptions](jsonserialization/writingoptions.md)
  Options for writing JSON data.
- [class func isValidJSONObject(Any) -> Bool](jsonserialization/isvalidjsonobject(_:).md)
  Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/writejsonobject(_:to:options:error:))*