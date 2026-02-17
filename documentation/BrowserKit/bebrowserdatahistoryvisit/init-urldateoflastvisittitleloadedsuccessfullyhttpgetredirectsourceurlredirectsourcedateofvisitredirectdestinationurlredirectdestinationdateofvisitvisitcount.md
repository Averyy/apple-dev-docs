# init(url:dateOfLastVisit:title:loadedSuccessfully:httpGet:redirectSourceURL:redirectSourceDateOfVisit:redirectDestinationURL:redirectDestinationDateOfVisit:visitCount:)

**Framework**: BrowserKit  
**Kind**: init

Creates a record of a page visit that includes metadata and redirect information.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init(url: URL, dateOfLastVisit: Date, title: String?, loadedSuccessfully: Bool, httpGet: Bool, redirectSourceURL: URL?, redirectSourceDateOfVisit: Date?, redirectDestinationURL: URL?, redirectDestinationDateOfVisit: Date?, visitCount: Int)
```

## Parameters

- `url`: The URL of the visited page.
- `dateOfLastVisit`: The date someone last visited the page.
- `title`: The title of the visited page, or   if unavailable.
- `loadedSuccessfully`: A Boolean value that indicates whether the page loaded without errors.
- `httpGet`: A Boolean value that indicates whether the visit used an HTTP GET request.
- `redirectSourceURL`: A URL that redirects to the visited page, or   if the visit isn’t the destination of a redirect.
- `redirectSourceDateOfVisit`: The date someone navigates to the source URL, or   if the visit isn’t the destination of a redirect.
- `redirectDestinationURL`: The URL to which this page redirects, or   if the visit doesn’t redirect.
- `redirectDestinationDateOfVisit`: The date someone navigates to the redirected destination, or   if the visit doesn’t redirect.
- `visitCount`: The number of times someone visited this page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit/init(url:dateoflastvisit:title:loadedsuccessfully:httpget:redirectsourceurl:redirectsourcedateofvisit:redirectdestinationurl:redirectdestinationdateofvisit:visitcount:))*