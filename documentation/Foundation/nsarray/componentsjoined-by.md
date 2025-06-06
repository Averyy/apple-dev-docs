# componentsJoined(by:)

**Framework**: Foundation  
**Kind**: method

Constructs and returns an `NSString` object that is the result of interposing a given separator between the elements of the array.

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
func componentsJoined(by separator: String) -> String
```

#### Return Value

An `NSString` object that is the result of interposing `separator` between the elements of the array. If the array has no elements, returns an `NSString` object representing an empty string.

#### Discussion

For example, this code excerpt writes “`here be dragons`” to the console:

```objc
NSArray *pathArray = [NSArray arrayWithObjects:@"here", @"be", @"dragons", nil];
NSLog(@"%@",[pathArray componentsJoinedByString:@" "]);
```

##### Special Considerations

Each element in the array must handle `description`.

## Parameters

- `separator`: The string to interpose between the elements of the array.

## See Also

- [func components(separatedBy: String) -> [String]](nsstring/components(separatedby:)-238fy.md)
  Returns an array containing substrings from the receiver that have been divided by a given separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/componentsjoined(by:))*