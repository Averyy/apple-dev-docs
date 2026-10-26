# index(forSubKeyPath:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

The index into the array at the specified portion of the key path.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func index(forSubKeyPath subKeyPath: String) -> Int
```

```objc
- (NSUInteger) indexForSubKeyPath:(NSString *) subKeyPath;
```

#### Return Value

The index of the item in the array.

#### Discussion

For intents or responses that contain an array of values, use this method to determine which object in the array was specified. For example, if a parameter represented the first object in an array of messages returned by a search, specifying the string `messages` would return the value `0`.

## Parameters

- `subKeyPath`: The key path to a property containing an array or ordered set. For example, when retrieving a message from a set of search results, specify the string `messages`.

## See Also

### Managing Indexed Values
- [func setIndex(Int, forSubKeyPath: String)](./setindex%28_,forsubkeypath%29.md)
  Specifies which item of an array or ordered set to use for the parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/index(forsubkeypath:))*