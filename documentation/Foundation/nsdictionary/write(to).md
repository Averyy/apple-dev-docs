# write(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes a property list representation of the contents of the dictionary to a given URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func write(to url: URL) throws
```

```objc
- (BOOL) writeToURL:(NSURL *) url error:(NSError **) error;
```

## Discussion

This method recursively validates that all the contained objects are property list objects (instances of [`NSData`](../nsdata.md), [`NSDate`](../nsdate.md), [`NSNumber`](../nsnumber.md), [`NSString`](../nsstring.md), [`NSArray`](../nsarray.md), or [`NSDictionary`](../nsdictionary.md)) before writing out the file. The method throws an error if all the objects are not property list objects, because the resulting output wouldn’t be a valid property list.

If the dictionary’s contents are all property list objects, you can use the location written by this method to initialize a new dictionary with the instance method `NSDictionary/init(contentsOfURL:)-4pv16`.

If you need greater control over the property list representation, use [`PropertyListSerialization`](../propertylistserialization.md) instead.

For more information about property lists, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## Parameters

- `url`: The URL to which to write the dictionary.

## See Also

### Storing Dictionaries
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes a property list representation of the contents of the dictionary to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/write(to:))*