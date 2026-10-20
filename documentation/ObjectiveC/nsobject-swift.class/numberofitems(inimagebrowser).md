# numberOfItems(inImageBrowser:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the number of records managed by the data source object.

**Availability**:
- macOS

## Declaration

```swift
func numberOfItems(inImageBrowser aBrowser: IKImageBrowserView!) -> Int
```

```objc
- (NSUInteger) numberOfItemsInImageBrowser:(IKImageBrowserView *) aBrowser;
```

#### Return Value

The number of records managed by the image browser view.

#### Discussion

Your data source must implement this method. An  [`IKImageView`](../../Quartz/ikimageview.md) object uses this method to determine how many cells it should create and display.

## Parameters

- `aBrowser`: An image browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/numberofitems(inimagebrowser:))*