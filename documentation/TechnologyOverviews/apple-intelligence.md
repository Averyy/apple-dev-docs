# Apple Intelligence

**Framework**: Technology Overviews

Adopt intelligent features, like Writing Tools and Genmoji, and help people search with Visual Intelligence.

#### Overview

Apple Intelligence is the personal intelligence system that drives built-in experiences, like Writing Tools, Image Playground, Visual Intelligence, and Genmoji. Apple Intelligence can make people’s experience with Apple devices more powerful, by making it easier to create content and interact with system features like Siri and Core Spotlight.

In most cases, you don’t need to do a lot to support Apple Intelligence features in your app. If you build your apps using system frameworks, you get many Apple Intelligence features for free. When you need more control, you can customize those features to create an experience that better suits your needs. For example, Writing Tools allows you to customize the type of content it generates for your text view.

When you want to enhance your features by using the on-device large language model powering Apple Intelligence, see [`Foundation Models`](foundation-models.md).

#### Add Visual Searching Capabilities

To help people find more information about the places and objects around them, [`Integrating your app with visual intelligence`](https://developer.apple.com/documentation/VisualIntelligence/integrating-your-app-with-visual-intelligence). People can use visual intelligence to receive information about objects they scan using the Camera Control [`on supported iPhone models`](https://developer.apple.comhttps://support.apple.com/guide/iphone/use-the-camera-control-iph0c397b154/ios). The framework provides information about what it detects, and uses App Intents to exchange that information with your app.

#### Enhance Peoples Writing Process in Your App

To help people improve the quality of their writing, add proofreading and rewriting tools to your app by adopting the Writing Tools API. The standard system text views already integrate support for Writing tools, and you can customize the experience to suit your app’s needs. You can also add Writing Tools support to your app’s [`Adding Writing Tools support to a custom UIKit view`](https://developer.apple.com/documentation/UIKit/adding-writing-tools-support-to-a-custom-uiview) using the provided APIs. When adding Writing Tools to your app:

- Adopt attributed strings as the backing store for your text content.
- Display text using the standard text views whenever possible, and use the configuration options to [`Customizing Writing Tools behavior for UIKit views`](https://developer.apple.com/documentation/UIKit/customizing-writing-tools-behavior-for-system-views).
- Use the Writing Tools API if you have a [`UIWritingToolsResultOptions`](https://developer.apple.com/documentation/UIKit/UIWritingToolsResultOptions) or can’t use the system text views.

#### Generate Creative Images From a Concept

To provide a way for people to personalize images, add support for [`Image Playground`](https://developer.apple.com/documentation/ImagePlayground). The framework provides the same interface you see in the [`Image Playground`](https://developer.apple.comhttps://apps.apple.com/us/app/image-playground/id6479176117) app, and lets people generate custom images by typing in what they want, or pairing an existing image with a description. The framework passes that information through an Apple Intelligence model to generate a stylized image for you to use in your app, like for a profile photo.

Your app can also [`ImageCreator`](https://developer.apple.com/documentation/ImagePlayground/ImageCreator), by taking the same type of input to generate images asynchronously and return them to your app.

#### Manage Genmoji in Your Apps Text

With Apple Intelligence, people can create Genmoji — custom emoji — by simply describing what they want it to look like. If your app supports text, Genmoji can be part of that the text content a person provides.

Because people create Genmoji in the strings they type, you typically don’t do anything with Genmoji directly. Standard text views handle Genmoji automatically by saving them as a [`NSAdaptiveImageGlyph`](https://developer.apple.com/documentation/UIKit/NSAdaptiveImageGlyph). When you want to persist text from a text view to disk, you might need to handle Genmoji in your file format. You need to look for Genmoji attachments when you implement your custom text views to display it correctly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/apple-intelligence)*