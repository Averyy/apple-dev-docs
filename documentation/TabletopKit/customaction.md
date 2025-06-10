# CustomAction

**Framework**: TabletopKit  
**Kind**: protocol

A protocol that represents an action whose behavior is implemented outside of TabletopKit. A custom action that can be applied to a `TableState`.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol CustomAction
```

## Topics

### Initializers
- [init?(from: some TabletopAction)](customaction/init(from:).md)
  Creates an instance of `CustomAction` initialized from the provided `TabletopAction`. If the provided action is not a custom action, this initializer returns `nil`.
### Instance Methods
- [func apply(table: inout TableState)](customaction/apply(table:).md)
  Implement this function to perform the changes to the table state that this action represents. It is important that the code performed in this function is only a function of the provided table state and the data of the action instance.
- [func validate(snapshot: TableSnapshot) -> Bool](customaction/validate(snapshot:).md)
  Implement this function to detect whether the action is valid and should be applied given the state of the table represented by `snapshot`. If not implemented, the action is always considered valid. It is important that the validation for a given action is only a function of the given snapshot and the data of the action instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/customaction)*