# validateValue(_:forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method

Indicates whether the value specified by a given pointer is not valid for a given key path relative to the receiver.

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
func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws
```

#### Discussion

In Swift, this method throws an error if the value isn’t valid.  In Objective-C, it returns a Boolean value.

The default implementation of this method gets the destination object for each relationship using [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) and returns the result of calling the [`validateValue(_:forKey:)`](nsobject-swift.class/validatevalue(_:forkey:).md) method for the property.

## Parameters

- `ioValue`: A pointer to a new value for the property identified by  . This method may modify or replace the value in order to make it valid.
- `inKeyPath`: The name of one of the receiver’s properties. The key path must specify an attribute or a to-one relationship. The key path has the form   (with one or more relationships); for example   or  .

## See Also

- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](nsobject-swift.class/validatevalue(_:forkey:).md)
  Indicates whether the value specified by a given pointer is valid, or can be made valid, for the property identified by a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkeypath:))*