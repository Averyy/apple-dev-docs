# data(fromPropertyList:format:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSData` object containing a given property list in a specified format.

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
class func data(fromPropertyList plist: Any, format: PropertyListSerialization.PropertyListFormat, options opt: PropertyListSerialization.WriteOptions) throws -> Data
```

```objc
+ (NSData *) dataWithPropertyList:(id) plist format:(NSPropertyListFormat) format options:(NSPropertyListWriteOptions) opt error:(NSError **) error;
```

#### Return Value

An `NSData` object containing `plist` in the format specified by `format`.

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `plist`: A property list object.
- `format`: A property list format. For possible values, see [`PropertyListSerialization.PropertyListFormat`](./propertylistformat.md).
- `opt`: The `opt` parameter is currently unused. No options should be specified.

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)
### Serializing a Property List
- [class func writePropertyList(Any, to: OutputStream, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions, error: NSErrorPointer) -> Int](./writepropertylist%28_,to,format,options,error%29.md)
  Writes a property list to the specified stream.
- [PropertyListSerialization.WriteOptions](./writeoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/data(frompropertylist:format:options:))*