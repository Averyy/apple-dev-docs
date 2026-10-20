# title

**Framework**: Background Tasks  
**Kind**: property  
**Role**: Instance Property

The localized task title displayed to a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var title: String { get set }
```

```objc
@property (copy, nonnull) NSString * title;
```

#### Discussion

Define the value of this property as a parameter to the request initializer:  [`init(identifier:title:subtitle:)`](./init%28identifier,title,subtitle%29.md).

## See Also

### Titling the task
- [var subtitle: String](./subtitle.md)
  The localized subtitle displayed to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/title)*