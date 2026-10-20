# classNameDecoded(forArchiveClassName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
func classNameDecoded(forArchiveClassName inArchiveName: String) -> String
```

```objc
- (NSString *) classNameDecodedForArchiveClassName:(NSString *) inArchiveName;
```

#### Return Value

The name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is `nameInArchive`. Returns `nameInArchive` unless a substitute name has been specified using the instance method (not the class method) [`decodeClassName(_:asClassName:)`](./decodeclassname%28_,asclassname%29-swift.method.md).

## Parameters

- `inArchiveName`: The ostensible name of a class in an archive.

## See Also

### Substituting classes or objects
- [class func classNameDecoded(forArchiveClassName: String) -> String](./classnamedecoded%28forarchiveclassname%29-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [class func decodeClassName(String, asClassName: String)](./decodeclassname%28_,asclassname%29-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func decodeClassName(String, asClassName: String)](./decodeclassname%28_,asclassname%29-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func replace(Any, with: Any)](./replace%28_,with%29.md)
  Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method)*