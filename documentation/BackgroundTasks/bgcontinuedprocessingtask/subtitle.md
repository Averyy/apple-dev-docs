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
var subtitle: String { get }
```

```objc
@property (copy, readonly) NSString * subtitle;
```

#### Discussion

Define the value of this property as a parameter to the request initializer:  [`init(identifier:title:subtitle:)`](../bgcontinuedprocessingtaskrequest/init%28identifier,title,subtitle%29.md). After that, this property is read only, however you can update the subtitle by calling [`updateTitle(_:subtitle:)`](./updatetitle%28_,subtitle%29.md).

## See Also

### Titling the task
- [var title: String](./title.md)
  The localized title displayed to a person.
- [func updateTitle(String, subtitle: String)](./updatetitle%28_,subtitle%29.md)
  Update the task title and subtitle that the system displays to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask/subtitle)*