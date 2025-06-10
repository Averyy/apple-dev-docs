# actions

**Framework**: CarPlay  
**Kind**: property

The actions that the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var actions: [CPTextButton] { get set }
```

#### Discussion

Assign a new array to this property to update the actions that the template displays. The template can display three actions maximum. If the array contains more actions, the template uses only the first three.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationtemplate/actions)*