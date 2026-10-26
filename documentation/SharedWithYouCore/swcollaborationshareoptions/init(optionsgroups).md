# init(optionsGroups:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and initializes a collaboration share options object with the array of groups.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(optionsGroups: [SWCollaborationOptionsGroup])
```

```objc
- (instancetype) initWithOptionsGroups:(NSArray<SWCollaborationOptionsGroup *> *) optionsGroups;
```

## Parameters

- `optionsGroups`: An array of [`SWCollaborationOptionsGroup`](../swcollaborationoptionsgroup.md) objects to customize how the system shares the collaboration.

## See Also

### Creating share options
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates and initializes a collaboration share options object.
- [init(optionsGroups: [SWCollaborationOptionsGroup], summary: String)](./init%28optionsgroups,summary%29.md)
  Creates and initializes a collaboration share options object the array of groups and a summary string.
- [+ shareOptionsWithOptionsGroups:](./shareoptionswithoptionsgroups_.md)
  Creates and initializes a collaboration share options object with the array of groups.
- [+ shareOptionsWithOptionsGroups:summary:](./shareoptionswithoptionsgroups_summary_.md)
  Creates and initializes a collaboration share options object the array of groups and a summary string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationshareoptions/init(optionsgroups:))*