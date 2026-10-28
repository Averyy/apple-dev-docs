# controller(_:sectionIndexTitleForSectionName:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the name for a given section.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, sectionIndexTitleForSectionName sectionName: String) -> String?
```

```objc
- (NSString *) controller:(NSFetchedResultsController *) controller sectionIndexTitleForSectionName:(NSString *) sectionName;
```

## Return Value

The string to use as the name for the specified section.

## Discussion

This method does not enable change tracking. It is only needed if a section index is used.

If the delegate doesn’t implement this method, the default implementation returns the capitalized first letter of the section name (see [`sectionIndexTitle(forSectionName:)`](../nsfetchedresultscontroller/sectionindextitle%28forsectionname%29.md) in `NSFetchedResultsController`).

## Parameters

- `controller`: The fetched results controller that sent the message.
- `sectionName`: The default name of the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:sectionindextitleforsectionname:))*