# title(for:identifier:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate to request the title of the menu item for the action.

**Availability**:
- macOS

## Declaration

```swift
func title(for person: ABPerson!, identifier: String!) -> String!
```

```objc
- (NSString *) titleForPerson:(ABPerson *) person identifier:(NSString *) identifier;
```

## Return Value

The title of the menu item for the action.

## Discussion

If the property returned by [`actionProperty()`](./actionproperty%28%29.md) is a multivalue property, `identifier` contains the unique identifier of the value selected.

## Parameters

- `person`: The person on which the action will be taken.
- `identifier`: The unique identifier of the value for which the menu item will be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/title(for:identifier:))*