# CFReadStreamSetProperty(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the value of a property for a stream.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFReadStreamSetProperty(_ stream: CFReadStream!, _ propertyName: CFStreamPropertyKey!, _ propertyValue: CFTypeRef!) -> Bool
```

```c
extern Boolean CFReadStreamSetProperty(CFReadStreamRef stream, CFStreamPropertyKey propertyName, CFTypeRef propertyValue);
```

## Return Value

`TRUE` if `stream` recognizes and accepts the given property-value pair, otherwise`FALSE`.

## Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any interesting information about a stream. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Properties that can be set configure the behavior of the stream and may be modifiable only at particular times, such as before the stream has been opened. (In fact, you should assume that you can set properties only before opening the stream, unless otherwise noted.) To read the value of a property use [`CFReadStreamCopyProperty(_:_:)`](./cfreadstreamcopyproperty%28_,_%29.md), although some properties are write-only.

## Parameters

- `stream`: The stream to modify.
- `propertyName`: The name of the property to set. The available properties for standard Core Foundation streams are listed in [CFStream](./cfstream.md).
- `propertyValue`: The value to which to set the property `propertyName` for `stream`. The allowed data type of the value depends on the property being set.

## See Also

### Setting Stream Properties
- [func CFReadStreamSetClient(CFReadStream!, CFOptionFlags, CFReadStreamClientCallBack!, UnsafeMutablePointer<CFStreamClientContext>!) -> Bool](./cfreadstreamsetclient%28_,_,_,_%29.md)
  Assigns a client to a stream, which receives callbacks when certain events occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamsetproperty(_:_:_:))*