# init(optionsGroups:summary:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and initializes a collaboration share options object the array of groups and a summary string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(optionsGroups: [SWCollaborationOptionsGroup], summary: String)
```

```objc
- (instancetype) initWithOptionsGroups:(NSArray<SWCollaborationOptionsGroup *> *) optionsGroups summary:(NSString *) summary;
```

## Parameters

- `optionsGroups`: An array of [`SWCollaborationOptionsGroup`](../swcollaborationoptionsgroup.md) objects to customize how the system shares the collaboration.
- `summary`: A localized string to summarize the collaboration options.

## See Also

### Creating share options
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates and initializes a collaboration share options object.
- [convenience init(optionsGroups: [SWCollaborationOptionsGroup])](./init%28optionsgroups%29.md)
  Creates and initializes a collaboration share options object with the array of groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationshareoptions/init(optionsgroups:summary:))*