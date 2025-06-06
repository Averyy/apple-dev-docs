# Social

**Framework**: Social  
**Kind**: module

Post content to supported social networking services, using standard system interfaces.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+

#### Overview

On iOS and macOS, this framework provides a template for creating HTTP requests. On iOS only, the Social framework provides a generalized interface for posting requests on behalf of the user.

A common way to use this framework is:

- Create a network session.
- Get the activity feed for a user.
- Make a new post.
- Set properties on a post, add attachments, etc.
- Publish a post to an activity feed.

## Topics

### Composition Interfaces
- [class SLComposeServiceViewController](slcomposeserviceviewcontroller.md)
  A view controller that you present from your share app extension, allowing the user to compose social media posts.
- [class SLComposeViewController](slcomposeviewcontroller.md)
  A view controller that allows the user to compose social media posts.
### Server Communication
- [class SLRequest](slrequest.md)
  An object that you use to assemble an HTTP request for communicating with a social media service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Social)*