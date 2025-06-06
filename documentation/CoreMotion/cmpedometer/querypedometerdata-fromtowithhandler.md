# queryPedometerData(from:to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Retrieves the data between the specified start and end dates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
func queryPedometerData(from start: Date, to end: Date, withHandler handler: @escaping CMPedometerHandler)
```

#### Discussion

Use this method to retrieve historical pedestrian data between the specified dates. This method runs asynchronously and delivers the data to the block you provide. Only the past seven days worth of data is stored and available for you to retrieve. Specifying a start date that is more than seven days in the past returns only the available data.

It is safe to call this method at the same time that you are generating continuous updates using the [`startUpdates(from:withHandler:)`](cmpedometer/startupdates(from:withhandler:).md) method.

## Parameters

- `start`: The start date for the data you want. This parameter must not be  .
- `end`: The end date for the data you want. This parameter must not be  .
- `handler`: The block to execute with the resulting data. This block is called once on the same serial dispatch queue used to process continuous updates. This parameter must not be  . For information about this block, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometer/querypedometerdata(from:to:withhandler:))*