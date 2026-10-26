# Getting Ready to Publish and Manage Your Articles

**Framework**: Apple News  
**Role**: Article

Get set up for using the Apple News API.

#### Overview

Once you have created an Apple News Format article, you use the Apple News API to send a request to publish the article to the Apple News app. You can also send requests to manage the articles in your channel. For example, you can:

- Update articles that have already been published
- Promote articles in specific sections
- See the sections available in a channel
- Find a specific article
- Delete articles that you no longer want in your channel

##### Verify Your Channel Security Information

Make sure you have the following security information, which you received when you set up your channel:

- Channel name
- Channel ID
- API Key ID
- API Key Secret

If you don’t have this information, see [Use your CMS with News Publisher](https://support.apple.com/guide/news-publisher/apd88c8447e6).

To learn how the Apple News API keeps your content secure, see [About the Apple News Security Model](./about-the-apple-news-security-model.md). You’ll use the authentication steps as part of each request you make.

##### Get the Apple News API

Choose one of these options:

- Download the [Apple News API Client Utility](https://developer.apple.com/apple-news/download/Apple-News-API-CLI.zip) (a Ruby Gem). Follow the setup instructions provided in the README file to install, configure, and use the utility.
- Use the Apple News REST API. Write your own code to integrate the Apple News API with your content management system (CMS) in a way that’s compatible with your organization’s processes.

##### Send a Request for Each Task

Requests you send to the Apple News resource contain a method (`GET`, `POST`, `PUT`, or `DELETE`) and a URL with the required parameters. Requests also include all security information, headers, body, and other parts the endpoint requires.

For example, to publish an article, use the Create an Article endpoint that starts with the `POST` method and this URL:

```other
POST https://news-api.apple.com/channels/{channelId}/articles
```

##### Validate Responses

The Apple News API returns the following responses:

- An HTTP status code
- A list of HTTP headers
- A body that includes any error or warning codes

For a list of status codes, see [`Status`](https://developer.apple.com/documentation/applenewsapi/status); for an explanation of error codes, see [`Error`](https://developer.apple.com/documentation/applenewsapi/error).

## See Also

### Essentials
- [About the Apple News Security Model](./about-the-apple-news-security-model.md)
  Learn how the Apple News API authenticates clients, authorizes your news channel, and enforces confidentiality.
- [About Apple News API Field Types](./about-apple-news-api-field-types.md)
  Understand the standard field types used in the Apple News API.
- [Formatting Strings](./formatting-strings.md)
  Learn how to format strings to pass to the API client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/getting-ready-to-publish-and-manage-your-articles)*