# URL filters

**Framework**: Network Extension

Create a filter that analyzes full URLs, while preserving privacy.

#### Overview

URL filters allow you to filter URL requests by analyzing the full URL against your URL data set (containing URLs you want to block) and determining whether to allow or block access to the URL.

Network Extension URL Filter examines all URL requests sent via WebKit and the [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) API. You create and manage a URL filter by using the [`NEURLFilterManager`](neurlfiltermanager.md) API and implementing the [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) protocol as your app extension to fetch a Bloom filter onto the device. Network Extension performs URL filtering on your behalf with your URL data set, using both the Bloom filter on the device as well as an off-device database hosted on your Private Information Retrieval (PIR) server. The system first consults the Bloom filter for a quick URL check, and may perform off-device database lookups with your PIR server if necessary. With this appoach, Network Extension URL Filter provides a performant yet privacy-preserving solution for both consumer and managed deployments.

For an example of writing and configuring a URL filter extension, see the [`Filtering traffic by URL`](filtering-traffic-by-url.md) sample code project.

For browsers or any app that doesn’t use WebKit or [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), use the [`NEURLFilter`](neurlfilter.md) Participation API to voluntarily check URLs. Call the [`verdict(for:)`](neurlfilter/verdict(for:).md) method to check all URL requests and honor the returned verdict by failing the URL requests for blocked URLs.

## Topics

### URL filters
- [class NEURLFilterManager](neurlfiltermanager.md)
  A class you use to configure and control a URL filter.
- [protocol NEURLFilterControlProvider](neurlfiltercontrolprovider.md)
  A protocol that defines an object that’s responsible for fetching pre-filter data.
- [class NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)
  A class that defines app extension configurations for the URL Filter control provider app extension.
- [class NEURLFilter](neurlfilter.md)
  A class used to voluntarily validate URLs for apps that don’t use WebKit or the URL session API.
- [Filtering traffic by URL](filtering-traffic-by-url.md)
  Perform fast and robust filtering of full URLs by managing URL filtering configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/url-filters)*