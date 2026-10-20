# write(to:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes a property list representation of the contents of the dictionary to a given URL.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`write(to:)`](./write%28to%29.md) instead.

## Declaration

```swift
func write(to url: URL, atomically: Bool) -> Bool
```

```objc
- (BOOL) writeToURL:(NSURL *) url atomically:(BOOL) atomically;
```

#### Return Value

[`true`](../../Swift/true.md) if the location is written successfully, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method recursively validates that all the contained objects are property list objects (instances of `NSData`, `NSDate`, `NSNumber`, `NSString`, `NSArray`, or `NSDictionary`) before writing out the file, and returns [`false`](../../Swift/false.md) if all the objects are not property list objects, since the resultant output would not be a valid property list.

If the dictionary’s contents are all property list objects, the location written by this method can be used to initialize a new dictionary with the class method `NSDictionary/init(contentsOfURL:)-98pl3` or the instance method `NSDictionary/init(contentsOfURL:)-4pv16`.

If you need greater control over the property list representation, use [`PropertyListSerialization`](../propertylistserialization.md) instead.

For more information about property lists, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## Parameters

- `url`: The URL to which to write the dictionary.
- `atomically`: A flag that specifies whether the output should be written atomically.

  If `atomically` is [`true`](../../Swift/true.md), the dictionary is written to an auxiliary location, and then the auxiliary location is renamed to `url`. If `atomically` is [`false`](../../Swift/false.md), the dictionary is written directly to `url`. The [`true`](../../Swift/true.md) option guarantees that `url`, if it exists at all, won’t be corrupted even if the system should crash during writing. `atomically` is ignored if `url` is of a type that cannot be written atomically.

## See Also

### Storing Dictionaries
- [func write(to: URL) throws](./write%28to%29.md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes a property list representation of the contents of the dictionary to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/write(to:atomically:))*