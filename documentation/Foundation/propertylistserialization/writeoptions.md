# PropertyListSerialization.WriteOptions

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias WriteOptions = Int
```

```c
typedef NSUInteger NSPropertyListWriteOptions;
```

## See Also

### Serializing a Property List
- [class func data(fromPropertyList: Any, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions) throws -> Data](./data%28frompropertylist,format,options%29.md)
  Returns an `NSData` object containing a given property list in a specified format.
- [class func writePropertyList(Any, to: OutputStream, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions, error: NSErrorPointer) -> Int](./writepropertylist%28_,to,format,options,error%29.md)
  Writes a property list to the specified stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/writeoptions)*