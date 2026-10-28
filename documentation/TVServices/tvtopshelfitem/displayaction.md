# displayAction

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The action to perform when the user wants to see more information for the current item.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var displayAction: TVTopShelfAction? { get set }
```

```objc
@property (nonatomic, strong, nullable) TVTopShelfAction * displayAction;
```

## Discussion

In a carousel inteface, the second of two buttons invites the user to display additional details for the current item. The action object you assign to this property provides the title and image to use for that button. When selected, the system loads the action’s URL.

In a sectioned or inset interface, tvOS loads the URL for the specified action when the user selects the current item.

## See Also

### Assigning Actions to the Item
- [var playAction: TVTopShelfAction?](./playaction.md)
  The action to perform when the user wants to play the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/displayaction)*