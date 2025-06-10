# urlSession(_:dataTask:didReceive:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the data task has received some of the expected data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive data: Data)
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)

#### Discussion

Because the data object parameter is often pieced together from a number of different data objects, whenever possible, use the [`enumerateBytes(_:)`](nsdata/enumeratebytes(_:).md) method to iterate through the data rather than using the [`bytes`](nsdata/bytes.md) method (which flattens the data object into a single memory block).

This delegate method may be called more than once, and each call provides only data received since the previous call. The app is responsible for accumulating this data if needed.

## Parameters

- `session`: The session containing the data task that provided data.
- `dataTask`: The data task that provided data.
- `data`: A data object containing the transferred data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didreceive:))*