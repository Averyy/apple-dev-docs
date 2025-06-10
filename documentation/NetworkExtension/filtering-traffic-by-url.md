# Filtering traffic by URL

**Framework**: Network Extension

Perform fast and robust filtering of full URLs by managing URL filtering configurations.

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 234: [`Filter and tunnel network traffic with NetworkExtension`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc25/234/).

#### Configure the Sample Code Project

To configure the sample code project, do the following in Xcode:

1. Set the developer team for all targets to your team so Xcode automatically manages the provisioning profile. For more information, see [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).
2. Optionally build and run the Private Information Retrieval (PIR) server sample provided with the sample code download. If you have your own PIR server ready for use, you can use that instead.

## See Also

- [class NEURLFilterManager](neurlfiltermanager.md)
  A class you use to configure and control a URL filter.
- [protocol NEURLFilterControlProvider](neurlfiltercontrolprovider.md)
  A protocol that defines an object that’s responsible for fetching pre-filter data.
- [class NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)
  A class that defines app extension configurations for the URL Filter control provider app extension.
- [class NEURLFilter](neurlfilter.md)
  A class used to voluntarily validate URLs for apps that don’t use WebKit or the URL session API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/filtering-traffic-by-url)*