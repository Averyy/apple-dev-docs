# replace(_:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
func replace(_ object: Any, with newObject: Any)
```

```objc
- (void) replaceObject:(id) object withObject:(id) newObject;
```

#### Discussion

`newObject` can be of a different class from object, and the class mappings set by [`classNameDecoded(forArchiveClassName:)`](./classnamedecoded%28forarchiveclassname%29-swift.type.method.md) and [`decodeClassName(_:asClassName:)`](./decodeclassname%28_,asclassname%29-swift.method.md) are ignored.

## Parameters

- `object`: The archived object to replace.
- `newObject`: The object with which to replace `object`.

## See Also

### Substituting classes or objects
- [class func classNameDecoded(forArchiveClassName: String) -> String](./classnamedecoded%28forarchiveclassname%29-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [class func decodeClassName(String, asClassName: String)](./decodeclassname%28_,asclassname%29-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](./classnamedecoded%28forarchiveclassname%29-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func decodeClassName(String, asClassName: String)](./decodeclassname%28_,asclassname%29-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver/replace(_:with:))*