# validateValue(_:forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Indicates whether the value specified by a given pointer is not valid for a given key path relative to the receiver.

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
func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws
```

```objc
- (BOOL) validateValue:(id*) ioValue forKeyPath:(NSString *) inKeyPath error:(NSError **) outError;
```

## Discussion

In Swift, this method throws an error if the value isn’t valid.  In Objective-C, it returns a Boolean value.

The default implementation of this method gets the destination object for each relationship using [`value(forKey:)`](./value%28forkey%29.md) and returns the result of calling the [`validateValue(_:forKey:)`](./validatevalue%28_,forkey%29.md) method for the property.

## Parameters

- `ioValue`: A pointer to a new value for the property identified by `inKeyPath`. This method may modify or replace the value in order to make it valid.
- `inKeyPath`: The name of one of the receiver’s properties. The key path must specify an attribute or a to-one relationship. The key path has the form `relationship``.``property` (with one or more relationships); for example `department.name` or `department.manager.lastName`.

## See Also

### Validation
- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](./validatevalue%28_,forkey%29.md)
  Indicates whether the value specified by a given pointer is valid, or can be made valid, for the property identified by a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkeypath:))*