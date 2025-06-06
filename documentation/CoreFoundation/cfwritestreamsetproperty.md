# CFWriteStreamSetProperty(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the value of a property for a stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFWriteStreamSetProperty(_ stream: CFWriteStream!, _ propertyName: CFStreamPropertyKey!, _ propertyValue: CFTypeRef!) -> Bool
```

#### Return Value

`true` if `stream` recognizes and accepts the given property-value pair, `false` otherwise.

#### Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any interesting information about a stream. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Properties that can be set configure the behavior of the stream and may be modifiable only at particular times, such as before the stream has been opened. (In fact, you should assume that you can set properties only before opening the stream, unless otherwise noted.) To read the value of a property use [`CFWriteStreamCopyProperty(_:_:)`](cfwritestreamcopyproperty(_:_:).md), although some properties are write-only.

## Parameters

- `stream`: The stream to modify.
- `propertyName`: The name of the property to set. The available properties for standard Core Foundation streams are listed in Stream Properties.
- `propertyValue`: The value to which to set the property   for  . The allowed data type of the value depends on the property being set.

## See Also

- [func CFWriteStreamSetClient(CFWriteStream!, CFOptionFlags, CFWriteStreamClientCallBack!, UnsafeMutablePointer<CFStreamClientContext>!) -> Bool](cfwritestreamsetclient(_:_:_:_:).md)
  Assigns a client to a stream, which receives callbacks when certain events occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamsetproperty(_:_:_:))*