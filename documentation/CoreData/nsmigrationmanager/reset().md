# reset()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Resets the association tables for the migration.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func reset()
```

```objc
- (void) reset;
```

## Discussion

This method does not reset the source or destination contexts.

## See Also

### Aborting a Migration
- [func cancelMigrationWithError(any Error)](./cancelmigrationwitherror%28_%29.md)
  Cancels the migration with a given error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/reset())*