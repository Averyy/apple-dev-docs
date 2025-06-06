# JSONSerialization

**Framework**: Foundation  
**Kind**: class

An object that converts between JSON and the equivalent Foundation objects.

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
class JSONSerialization
```

#### Overview

You use the [`JSONSerialization`](jsonserialization.md) class to convert JSON to Foundation objects and convert Foundation objects to JSON.

To convert a Foundation object to JSON, the object must have the following properties:

- The top level object is an [`NSArray`](nsarray.md) or [`NSDictionary`](nsdictionary.md), unless you set the [`fragmentsAllowed`](jsonserialization/writingoptions/fragmentsallowed.md) option.
- All objects are instances of [`NSString`](nsstring.md), [`NSNumber`](nsnumber.md), [`NSArray`](nsarray.md), [`NSDictionary`](nsdictionary.md), or [`NSNull`](nsnull.md).
- All dictionary keys are instances of [`NSString`](nsstring.md).
- Numbers are neither `NaN` nor infinity.

Other rules may apply. Calling [`isValidJSONObject(_:)`](jsonserialization/isvalidjsonobject(_:).md) or attempting a conversion are the definitive ways to tell if the [`JSONSerialization`](jsonserialization.md) class can convert given object to JSON data.

> **Note**:  On iOS 7 and later and macOS 10.9 and later, [`JSONSerialization`](jsonserialization.md) is thread safe.

 On iOS 7 and later and macOS 10.9 and later, [`JSONSerialization`](jsonserialization.md) is thread safe.

## Topics

### Creating a JSON Object
- [class func jsonObject(with: Data, options: JSONSerialization.ReadingOptions) throws -> Any](jsonserialization/jsonobject(with:options:)-8demi.md)
  Returns a Foundation object from given JSON data.
- [class func jsonObject(with: InputStream, options: JSONSerialization.ReadingOptions) throws -> Any](jsonserialization/jsonobject(with:options:)-3afap.md)
  Returns a Foundation object from JSON data in a given stream.
- [JSONSerialization.ReadingOptions](jsonserialization/readingoptions.md)
  Options used when creating Foundation objects from JSON data.
### Creating JSON Data
- [class func data(withJSONObject: Any, options: JSONSerialization.WritingOptions) throws -> Data](jsonserialization/data(withjsonobject:options:).md)
  Returns JSON data from a Foundation object.
- [class func writeJSONObject(Any, to: OutputStream, options: JSONSerialization.WritingOptions, error: NSErrorPointer) -> Int](jsonserialization/writejsonobject(_:to:options:error:).md)
  Writes a given JSON object to a stream.
- [JSONSerialization.WritingOptions](jsonserialization/writingoptions.md)
  Options for writing JSON data.
- [class func isValidJSONObject(Any) -> Bool](jsonserialization/isvalidjsonobject(_:).md)
  Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class JSONEncoder](jsonencoder.md)
  An object that encodes instances of a data type as JSON objects.
- [class JSONDecoder](jsondecoder.md)
  An object that decodes instances of a data type from JSON objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization)*