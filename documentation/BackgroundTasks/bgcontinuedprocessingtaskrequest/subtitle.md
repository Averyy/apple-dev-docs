# subtitle

**Framework**: Background Tasks  
**Kind**: property  
**Role**: Instance Property

The localized subtitle displayed to a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var subtitle: String { get set }
```

```objc
@property (copy, nonnull) NSString * subtitle;
```

## Discussion

Define the value of this property as a parameter to the request initializer:  [`init(identifier:title:subtitle:)`](./init%28identifier,title,subtitle%29.md).

## See Also

### Titling the task
- [var title: String](./title.md)
  The localized task title displayed to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/subtitle)*