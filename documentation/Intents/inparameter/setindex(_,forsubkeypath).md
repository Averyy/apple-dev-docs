# setIndex(_:forSubKeyPath:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Specifies which item of an array or ordered set to use for the parameter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setIndex(_ index: Int, forSubKeyPath subKeyPath: String)
```

```objc
- (void) setIndex:(NSUInteger) index forSubKeyPath:(NSString *) subKeyPath;
```

## Discussion

When the key path for a parameter contains an array or ordered set, use this method to specify which object in that array or ordered set to use.

## Parameters

- `index`: The index of an object in the array or ordered set.
- `subKeyPath`: The path to the property containing an array or ordered set. For example, the key path for the messages property of an [`INSearchForMessagesIntentResponse`](../insearchformessagesintentresponse.md) object would be the string `messages`.

## See Also

### Managing Indexed Values
- [func index(forSubKeyPath: String) -> Int](./index%28forsubkeypath%29.md)
  The index into the array at the specified portion of the key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/setindex(_:forsubkeypath:))*