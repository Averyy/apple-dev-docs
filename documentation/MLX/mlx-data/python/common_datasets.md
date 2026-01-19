---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/common_datasets.html
---

# Common Datasets

**

- [.rst](../_sources/python/common_datasets.rst)
- **

.pdf

**

# Common Datasets

 Table of contents 

# Common Datasets

Although MLX data is designed to make it easy to implement your own data
pipeline directly in your own scripts, we provide some utility functions that
make it easy to access some commonly used datasets.

For instance the following is an example interaction that loads the MNIST and
the wikitext-103 datasets.

```
import mlx.data as dx
from mlx.data.datasets import load_mnist, load_wikitext_lines
from mlx.data.tokenizer_helpers import read_trie_from_vocab

mnist = load_mnist()
print(mnist)
# Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz 9.5MiB (15.1MiB/s)
# Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz 1.6MiB (12.9MiB/s)
# Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz 32.0KiB (17.1MiB/s)
# Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz 8.0KiB (26.6MiB/s)
# Buffer(size=60000, keys={'label', 'image'})

mnist_iter = (
    mnist
    .shuffle()
    .to_stream()
    .key_transform("image", lambda x: (x.astype("float32") / 255).ravel())
    .batch(128)
    .prefetch(4, 2)
)
print(next(mnist_iter)["image"].shape)
# (128, 784)

wiki = load_wikitext_lines(split="train")
print(wiki)
# Downloading https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-raw-v1.zip 183.1MiB (9.9MiB/s)
# Computing hash of ..../.cache/mlx.data/wikitext/wikitext-103-raw-v1.zip |████████████████████████████████████████| 183.1MiB / 183.1MiB (1.0GiB/s)
# Extracting ..../.cache/mlx.data/wikitext/wikitext-103-raw-v1.zip 517.9MiB (318.2MiB/s)
# Stream()

workers = 8
trie = read_trie_from_vocab("/path/to/vocab.txt")
wiki_iterator = (
    wiki
    .tokenize("line", trie, output_key="tokens")
    .filter_key("tokens")
    .prefetch(512, workers)
    .batch(128, dim=dict(tokens=0))  # gather everything in a big array of tokens
    .sliding_window("tokens", 1025, 1025)
    .shape("tokens", "tokens_length", 0)
    .batch(32)  # actual batch size
    .prefetch(2, 1)
)
# The above can be iterated at approximately 2.5M tok/s on an M2 Macbook Air.
```

| load_mnist([root, train]) | Load a buffer with the MNIST dataset. |
| --- | --- |
| load_fashion_mnist([root, train]) | Load a buffer with the Fashion-MNIST dataset. |
| load_cifar10([root, train, quiet, ...]) | Load a buffer with the CIFAR-10 dataset. |
| load_cifar100([root, train, quiet, ...]) | Load a buffer with the CIFAR-100 dataset. |
| load_imagenet([root, split, quiet, ...]) | Load the ImageNet dataset from the downloaded archives. |
| load_images_from_folder(image_folder) | Load images from a folder. |
| load_librispeech([root, split, quiet, ...]) | Load the librispeech dataset directly from the TAR archive. |
| load_libritts_r([root, split, quiet, ...]) | Load the LibriTTS-R dataset directly from the TAR archive. |
| load_wikitext_lines([root, split, subset, ...]) | Fetch the WikiText dataset and load it as a stream of lines. |
| load_speechcommands([root, split, quiet, ...]) | Load the Speech Commands (v0.0.2) [1] dataset directly from the TAR archive. |
